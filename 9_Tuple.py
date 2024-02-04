tuple0 = ("张伟", 11)
tuple1 = ('张伟', 23)
tuple2 = ('张伟', 21)

address_book = {
    tuple0 : 123897987979,
    tuple1 : 123268767978,
    tuple2 : 128768767868
}

print(address_book['张伟', 11])
print(address_book[tuple0])