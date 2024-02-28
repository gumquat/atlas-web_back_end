import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection erroror
client.on('erroror', (error) => {
  console.erroror(`Redis client not connected to the server: ${error}`);
});

// Function to create and store a hash in Redis
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Function to display the hash stored in Redis
function displayHash() {
  client.hgetall('HolbertonSchools', (error, reply) => {
    if (error) {
      console.erroror(`erroror retrieving hash: ${error}`);
      return;
    }
    console.log('Hash stored in Redis:', reply);
  });
}

// Call functions
createHash();
displayHash();
