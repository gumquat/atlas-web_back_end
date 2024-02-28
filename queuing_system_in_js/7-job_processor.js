import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of job
  job.progress(0, 100);

  // If phoneNumber is blacklisted, fail the job
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
  } else {
    // Track progress to 50%
    job.progress(50, 100);
    // Log sending notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    // Complete the job
    done();
  }
}

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from job
  const { phoneNumber, message } = job.data;
  // Call sendNotification function
  sendNotification(phoneNumber, message, job, done);
});
