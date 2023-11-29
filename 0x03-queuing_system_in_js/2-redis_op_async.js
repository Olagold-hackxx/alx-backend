import { createClient, print } from 'redis';
import { promisify } from "util";

const client = promisify(createClient())
client
    .on('error', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

async function setNewSchool (schoolName, value) {
    await client.set(schoolName, value, (err, reply) => print(`Reply: ${reply}`))
}

async function displaySchoolValue(schoolName) {
	await client.get(schoolName, (err, reply) => console.log(reply))
}

await displaySchoolValue('Holberton');
await setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
