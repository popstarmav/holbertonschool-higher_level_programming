#!/usr/bin/node
//  Using const for constant values
const args = process.argv.slice(2);

// Check number of arg and print message
if (args.length === 0)
{
	console.log('No argument');
}
else if (args.length === 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
