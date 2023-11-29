import { createClient, print } from 'redis';
const client = createClient()
client
    .on('error', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
    client.set(schoolName, value, (err, reply) => print(`Reply: ${reply}`))
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => console.log(reply))
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
