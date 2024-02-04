

# Create your tests here.
class dd(dict):
    def get(self, __key,  default = None):
        res = super().get(__key, default=default)
        return res




ddd = dd()
aa = dd.get('ffdfd')
print(aa)