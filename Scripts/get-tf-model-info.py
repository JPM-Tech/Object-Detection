import tensorflow as tf
print("tensorflow version: ", tf.__version__)
gf = tf.GraphDef()   
m_file = open('saved_model.pb','rb')
gf.ParseFromString(m_file.read())

# TODO: figure out the details from the model, such as the Input Type, Bias, and Scale of the images, as well as the name of the output

with open('somefile.txt', 'a') as the_file:
    for n in gf.node:
        the_file.write(n.name+'\n')

file = open('somefile.txt','r')
data = file.readlines()
print("output name = ")
print(data[len(data)-1])

print("Input name = ")
file.seek ( 0 )
print(file.readline())