import hashlib

def find_hash_algorithm(plaintext, ciphertext):
    algorithms = hashlib.algorithms_guaranteed  # 获取Python支持的所有散列算法

    for algorithm in algorithms:
        hash_object = hashlib.new(algorithm)  # 创建哈希对象
        hash_object.update(plaintext.encode())  # 更新哈希对象的内容为明文的字节表示

        if hash_object.hexdigest() == ciphertext:
            return algorithm

    return None

# 输入明文和密文
plaintext = input("请输入明文：")
ciphertext = input("请输入密文：")

# 查找匹配的散列方法
matching_algorithm = find_hash_algorithm(plaintext, ciphertext)

if matching_algorithm:
    print("匹配成功！加密方法和函数名称为：", matching_algorithm)
else:
    print("没有找到匹配的散列方法。")