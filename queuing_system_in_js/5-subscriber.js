import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Event listener for successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Event listener for message received on the channel
subscriber.on('message', (channel, message) => {
  console.log(`Received message from channel ${channel}: ${message}`);
  
  // Check if message is KILL_SERVER, if so, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
