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

// Event listener for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a given school
function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${error}`);
      return;
    }
    console.log(`Value for ${schoolName}: ${reply}`);
  });
}

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
