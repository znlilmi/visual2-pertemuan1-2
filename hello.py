# Membuat segitiga
def segitiga(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

# Menggunakan fungsi segitiga
segitiga(5)
