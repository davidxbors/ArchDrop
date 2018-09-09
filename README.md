# ArchDrop

It's a program that tries to emulate AirDrop behaviour, but cross-platform, by using sockets library.

## Why sockets?

Because:

* It's simple
* It's available in multiple languages, and this is good for the fact that it should be cross-platform

## Idea!

The way this app should work:

### When you start the app

When you start the app an server script runs, also all the [devices on your list][dol] are checked, to see who's online.

### When someone sends smth to you

The server script will get triggered, it will receive the data and do the proper thing with it

### When you send smth to someone

The client side sends the data you want to the server script running on the destination device

### <a name="dol"></a> Devices on your list

Each instance has a list with friend devices, so it will be easier to send data to them. 

The list consists in their \<ip / mac (not sure yet>:<port>

