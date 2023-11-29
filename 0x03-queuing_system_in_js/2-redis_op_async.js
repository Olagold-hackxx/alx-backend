import { createClient, print } from 'redis';
import { promisify } from "util";

const client = createClient()
client
    .on('error', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
    client.set(schoolName, value, (err, reply) => print(`Reply: ${reply}`))
}

const asyncGet = promisify(client.get).bind(client)
async function displaySchoolValue(schoolName) {
    const reply = await asyncGet(schoolName)
    console.log(reply)
}

async function run(){
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}
run()
