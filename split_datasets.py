
'''
1. read the whole files under a certain folder
2. chose 200 files randomly
3. move them to another folder and save
'''
import os, random, shutil
import glob

TEST_PERCENTAGE = 30
names = []
def  copyFile(image_dir, image_tar_dir_test, image_tar_dir_train,):
    # pathDir = os.listdir(image_dir)
    image_lists = os.listdir(image_dir)
    lengths_lists = len(image_lists)
#########################test################################################################
    test_names = random.sample(image_lists, int(lengths_lists * TEST_PERCENTAGE / 100))
    for name in image_lists:
        na = name[:-4]
        if name in test_names:
            shutil.copy(image_dir + name, image_tar_dir_test + name)
            # shutil.copy(xml_dir + na + '.xml', xml_tar_dir_test + na + '.xml')

#########################train################################################################
        else:
            shutil.copy(image_dir + name, image_tar_dir_train + name)
            # shutil.copy(xml_dir + na + '.xml', xml_tar_dir_train + na + '.xml')

            print("now {} is being proceeding.".format(name))

if __name__ == '__main__':

######copy images and xmls to split_datasets
    dataset_path = './DataSet/NWPU-RESISC45/'
    classes = os.listdir(dataset_path)
    for name in classes:
        image_dir = dataset_path + name + '/'
        image_tar_dir_test = './dataset/val/' + name + '/'
        image_tar_dir_train = './dataset/train/' + name + '/'
        if not os.path.isdir(image_tar_dir_test):
           os.makedirs(image_tar_dir_test)
        if not os.path.isdir(image_tar_dir_train):
           os.makedirs(image_tar_dir_train)
        copyFile(image_dir, image_tar_dir_test, image_tar_dir_train)



######creat train.txt and test.txt to split_datasets
    # path = './VOC2012/Annotations'
    # img_list = os.listdir(path)
    # txt_path = './VOC2012/ImageSets/Main'
    # if not os.path.exists(txt_path):
    #    os.makedirs(txt_path)
    #
    # lengths_lists = len(img_list)
    # test_names = random.sample(img_list, int(lengths_lists * TEST_PERCENTAGE / 100))
    # # filename = './test'
    # with open(txt_path + '/trainval.txt', 'w') as f:
    #     for image_id in img_list:
    #         if image_id in test_names:
    #             continue
    #         else:
    #             image_id = image_id.split('.')[0]
    #             f.write('%s\n' % image_id)
    # with open(txt_path + '/test.txt', 'w') as f:
    #     for image_id in test_names:
    #         image_id = image_id.split('.')[0]
    #         f.write('%s\n' % image_id)


