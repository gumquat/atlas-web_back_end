import redis from 'redis';

// make a Redis client
const client = redis.createClient(
  {
    host: '1237.0.0.1',
    port: 6379
  }
);

// event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// event listener for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});
