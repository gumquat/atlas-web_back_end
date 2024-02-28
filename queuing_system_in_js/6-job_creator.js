import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.'
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData);

// Event listener for successful job creation
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// Event listener for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
