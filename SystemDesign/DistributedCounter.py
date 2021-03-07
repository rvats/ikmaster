import time
def counter():
    start = time.time()
    counter = 0
    while counter < 1000000001:
        counter+=1
        print(counter)
    end = time.time()
    print(end - start)

def distributedCounter()(self, doc_ref):
    """Increment a randomly picked shard."""
    doc_id = random.randint(0, self._num_shards - 1)

    shard_ref = doc_ref.collection("shards").document(str(doc_id))
    return shard_ref.update({"count": firestore.Increment(1)})
distributedCounter()