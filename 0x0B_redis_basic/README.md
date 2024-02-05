# Pre-work reading materials

Redis is an open-source, in-memory data structure store that serves as a key-value database, cache, and message broker. It is often referred to as a "data structure server" because it allows developers to use various data structures like strings, hashes, lists, sets, and more, and perform operations on these data structures.

Key features of Redis include:

1. **In-Memory Data Storage:** Redis stores data in RAM, which allows for fast read and write operations. This makes it suitable for use cases where low-latency access to data is crucial.

2. **Persistence:** While Redis primarily operates in-memory, it supports persistence by periodically saving data to disk. This enables data recovery in case of server restarts or failures.

3. **Data Structures:** Redis provides a variety of data structures such as strings, hashes, lists, sets, and sorted sets. These structures come with their own set of operations, making it versatile for different use cases.

4. **Atomic Operations:** Redis ensures atomicity for many operations, meaning that operations are executed as a single, indivisible unit. This is useful for maintaining data consistency.

5. **Pub/Sub Messaging:** Redis supports Publish/Subscribe (Pub/Sub) messaging paradigm, allowing different parts of an application to communicate with each other by publishing and subscribing to channels.

6. **High Performance:** Due to its in-memory nature and optimized C codebase, Redis is known for its high performance and low latency.

7. **Versatility:** Redis can be used for various use cases, including caching, session storage, real-time analytics, leaderboard management, job queues, and more.

Developers often use Redis to improve the performance of applications by caching frequently accessed data, managing real-time analytics, or facilitating communication between different components of a distributed system.

It's important to note that while Redis is powerful and efficient for certain use cases, it may not be suitable for all scenarios, especially when the dataset is too large to fit into memory. In such cases, other types of databases that focus on disk-based storage might be more appropriate.

# Problems
## 0. Writing strings to Redis - main.py, exercise.py
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.
## 1. Reading from Redis and recovering original type - exercise.py
* Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

Create a get method that take a key string argument and an optional Callable argument named 'fn'. This callable will be used to convert the data back to the desired format.

Conserve the original Redis.get behavior if the key does not exist.

Implement 2 new methods: 'get_str' and 'get_int' that will automatically parametrize Cache.get with the correct conversion function.
## 2. Incrementing values - 2-main.py, exercise.py
* The first argument of the wrapped function will be self which is the instance itself, which lets you access the Redis instance.
* When defining a decorator it is useful to use functool.wraps to conserve the original function’s name, docstring, etc.
Implement a system to count how many times methods of the Cache class are called.

Above Cache define a count_calls decorator that takes a single method Callable argument and returns a Callable.

As a key, use the qualified name of method using the '__qualname__' dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

Decorate Cache.store with count_calls.

## 3. Storing lists - 3-main.py
* Redis commands RPUSH, LPUSH, LRANGE, etc.
* Redis can only store strings, bytes and numbers.

Define a call_history decorator to store the history of inputs and outputs for a particular function.
Everytime the original function will be called, add its input parameters to one list in redis, and store its output into another list.

In call_history, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.

'call_history' has a single parameter named method that is a Callable and returns a Callable.

In the new function that the decorator will return, use rpush to append the input arguments. Use 'str(args)' to normalize. Ignore potential 'kwargs' for now.

Execute the wrapped function to retrieve the output. Store the output using rpush in the "...:outputs" list, then return the output.

Decorate Cache.store with call_history.

## 4. Retrieving lists - exercise.py
* Use 'lrange' and 'zip' to loop over inputs and outputs.

Implement a replay function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:
```
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```