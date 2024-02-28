import redis from 'redis';

// make a Redis client
const client = redis.createClient();

// event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// event listener for connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
