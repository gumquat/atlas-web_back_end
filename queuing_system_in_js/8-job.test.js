import kue from 'kue';
import { createPushNotificationsJobs } from './8-job'; // Assuming the function is exported from 8-job.js

// Mocking the queue
jest.mock('kue', () => {
  const { EventEmitter } = require('events');
  const queue = {
    create: jest.fn(() => ({
      save: jest.fn(),
      on: jest.fn(),
    })),
    testMode: true,
    jobs: [],
    process: () => {},
    on: jest.fn(),
  };
  return {
    createQueue: jest.fn(() => queue),
  };
});

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a new queue instance for each test
    queue = kue.createQueue();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    kue.jobs = [];
    kue.testMode = false;
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).toThrow('Jobs is not an array');
  });

  it('should create jobs in the queue with correct data', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Message 1' },
      { phoneNumber: '4153518781', message: 'Message 2' },
      { phoneNumber: '4153518782', message: 'Message 3' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.create).toHaveBeenCalledTimes(jobs.length);
    jobs.forEach((jobData, index) => {
      expect(queue.create).toHaveBeenCalledWith('push_notification_code_3', jobData);
    });
  });

  // Add more test cases as needed
});
