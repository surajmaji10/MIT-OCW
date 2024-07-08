
## hash set in python
class HashSet(object):

    def __init__(self, buckets):
        self.num_buckets = buckets
        self.buckets_list = []
        for i in range(self.num_buckets):
            self.buckets_list.append([])

    def insert(self, value):
        idx = self.hash_fun(value)
        bucket = self.buckets_list[idx]
        if not self.member(value):
            bucket.append(value)
            return True
        else:
            return False

    def hash_fun(self, value):
        if type(value) == int:
            hash_val = value
            return hash_val % self.num_buckets
        elif type(value) == str:
            hash_val = 0
            s = 1
            for c in value:
                hash_val += s * ord(c)
                s += 1
            return hash_val % self.num_buckets
        elif type(value) == float:
            hash_val = int(value)
            return hash_val % self.num_buckets
        else:
            return 0

    def member(self, value):
        idx = self.hash_fun(value)
        bucket = self.buckets_list[idx]
        return value in bucket
    
    def remove(self, value):
        if not self.member(value):
            return False
        else:
            idx = self.hash_fun(value)
            bucket = self.buckets_list[idx]
            new_bucket = []
            for item in bucket:
                if item != value:
                    new_bucket.append(item)
            self.buckets_list[idx] = new_bucket
            # print(bucket, new_bucket)
            return True
      

# myset = HashSet()
# myset.insert(12)
# myset.insert(13)
# myset.insert(12345)
# print(myset.buckets_list)
# print(myset.remove(13))
# print(myset.member(13))
# print(myset.buckets_list)

myset = HashSet(17)
myset.insert("akash")
myset.insert("suraj")
myset.insert("anup")
myset.insert("mithu")
print(myset.buckets_list)
myset.remove("mithu")
print(myset.buckets_list)



            
    
    

