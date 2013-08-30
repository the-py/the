def r(x):
    raise Exception(x)

for i in ['which', 'I', 'want', 'to', 'test', 'when']:
    The.them.add(i)

The({'a': 1, 'b': 2}).should.have.property('a', 1)
print The(1).should.nt.be.an(str)
print The(1).which.I.want.to.test.should.nt.be.an(str)
print The(r).when.apply('hello world').should.throw('').when.apply('xxx').should.nt.throw('hello world')
