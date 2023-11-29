import { createClient, print } from 'redis';
import { promisify } from "util";

const client = promisify(createClient())
client
    .on('error', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

const name = "HolbertonSchools";
const values = {
	  Portland: 50,
	  Seattle: 80,
	  "New York": 20,
	  Bogota: 20,
	  Cali: 40,
	  Paris: 2,
};
for (const [key, val] of Object.entries(values)) {
	  client.hset(name, key, val, (err, reply) => redis.print(`Reply: ${reply}`));
}
client.hgetall(name, (err, data) => console.log(data));
