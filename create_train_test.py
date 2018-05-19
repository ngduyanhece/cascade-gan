import os

if __name__=='__main__':
    all_img = os.listdir(os.path.join('img','meiryo'))
    #let get 100 images as test and the last for training
    train_img = all_img[:-300]
    test_img = all_img[-300:]
    with open('train.txt', 'w') as the_file:
        for img in train_img:
            the_file.write(img + '\n')
    with open('test.txt', 'w') as the_file:
        for img in test_img:
            the_file.write(img + '\n')
