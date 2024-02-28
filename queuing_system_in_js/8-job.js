import kue from 'kue';

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Process each job
  jobs.forEach((jobData) => {
    // Create a job in the queue
    const job = queue.create('push_notification_code_3', jobData);

    // Event listener for successful job creation
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Event listener for job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Event listener for job failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Event listener for job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
}

// Example jobs data
const jobs = [
  { phoneNumber: '4153518780', message: 'Message 1' },
  { phoneNumber: '4153518781', message: 'Message 2' },
  { phoneNumber: '4153518782', message: 'Message 3' },
];

// Create a Kue queue
const queue = kue.createQueue();

// Call createPushNotificationsJobs function
createPushNotificationsJobs(jobs, queue);
