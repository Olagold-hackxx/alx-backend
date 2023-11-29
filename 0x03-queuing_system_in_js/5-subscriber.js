import { createClient, print } from 'redis';
import { promisify } from "util";

const client = createClient()
client
    .on('error', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');

// On message received
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
	client.unsubscribe();
	client.quit();
    }
});
