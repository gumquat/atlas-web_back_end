import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a given school asynchronously
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(`Value for ${schoolName}: ${reply}`);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err}`);
  }
}

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
