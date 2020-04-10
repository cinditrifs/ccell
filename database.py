import redis
import json

ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db='1')

'''=======================database user
Karena butuh buat di tampilin di tabel agen maka data yang dibutuhkan =
name :
id_agen : #buatmasuk
tlp_num : (sebenernya dalam proses asli dibutuhkan, tapi bisa gunain username aja)
pin :  #buat masuk
nanti buat lagi fungsi manggil untuk ngecreate data agen dan admin biar beda
sedangkan data admin yang dibutuhkan :
name :
username :
password :
'''

#admin
admin_001 = {'name' : 'Cindi Tri', 'username' : 'admin_001', 'password' : 1111}
admin_002 = {'name' : 'Canda Dwi', 'username' : 'admin_002', 'password' : 2222}
admin_003 = {'name' : 'Candy Four', 'username' : 'admin_003', 'password' : 3333 }

#agen
agen_001 = {'name' : 'Afny', 'id_agen' : 'agen_001', 'tlp_num' : '081276564738', 'pin': 1101}
agen_002 = {'name' : 'Nilatil Moena', 'id_agen' : 'agen_002', 'tlp_num' : '08123456789', 'pin': 1102}
agen_003 = {'name' : 'Novitasari', 'id_agen' : 'agen_003', 'tlp_num' : '089876567895', 'pin': 1103}
agen_004 = {'name' : 'Zakiyah Hamidah', 'id_agen' : 'agen_004', 'tlp_num' : '08234567898', 'pin': 1104}
agen_005 = {'name' : 'Diyah Anggraeny', 'id_agen' : 'agen_005', 'tlp_num' : '082345768909', 'pin': 1105}
agen_006 = {'name' : 'Rachel Haryawan', 'id_agen' : 'agen_006', 'tlp_num' : '08962543789', 'pin': 1106 }
agen_007 = {'name' : 'Muhammad Ardani', 'id_agen' : 'agen_007', 'tlp_num' : '08234567800', 'pin': 1107 }
agen_008 = {'name' : 'Zaidan Pratama', 'id_agen' : 'agen_008', 'tlp_num' : '08234567834', 'pin': 1108}
agen_009 = {'name' : 'Lazuardy Khatilistiwa', 'id_agen' : 'agen_009', 'tlp_num' : '08234556898', 'pin': 1109}
agen_010 = {'name' : 'Lisa Arief', 'id_agen' : 'agen_010', 'tlp_num' : '08434567898', 'pin': 1110}


'''=======================database produk
nanti buat lagi fungsi manggil untuk ngecreat data tiap operator
jadi kalo mau manggil tiap operator bisa
yang dibutuhin untuk nampilin harga
kode_produk :
detail :
harga :
'''
#INDOSAT
paket_1 = {'kode_produk': 'ISAT5', 'detail':'INDOSAT 5.000', 'harga': 5400}
paket_2 = {'kode_produk': 'ISAT10', 'detail':'INDOSAT 10.000', 'harga': 10950}
paket_3 = {'kode_produk': 'ISAT12', 'detail':'INDOSAT 12.000', 'harga': 12500}
paket_4 = {'kode_produk': 'ISAT15', 'detail':'INDOSAT 15.000', 'harga': 16100}
paket_5 = {'kode_produk': 'ISAT20', 'detail':'INDOSAT 20.000', 'harga': 20250}
paket_6 = {'kode_produk': 'ISAT50', 'detail':'INDOSAT 50.000', 'harga': 49.300}
paket_7 = {'kode_produk': 'ISAT100', 'detail':'INDOSAT 100.000', 'harga': 97300}
paket_8 = {'kode_produk': 'IT2', 'detail':'INDOSAT TLP 1 hari 1.000 menit', 'harga': 2200}
paket_9 = {'kode_produk': 'ITS', 'detail':'INDOSAT TLP SMS 1250+250 ALL', 'harga': 10300}
paket_10 = {'kode_produk': 'IT15', 'detail':'INDOSAT TELP 14H UNLIMITED + 30 MENIT', 'harga' : 20250}

#XL
paket_11 = {'kode_produk' : 'XL5', 'detail' : 'XL 5.000', 'harga' : 5990 }
paket_12 = {'kode_produk' : 'XL10', 'detail' : 'XL 10.000', 'harga' : 10990}
paket_13 = {'kode_produk' : 'XL25', 'detail' : 'XL 25.000', 'harga' : 24950}
paket_14 = {'kode_produk' : 'XL50', 'detail' : 'XL 50.000', 'harga' : 49700}
paket_15 = {'kode_produk' : 'XL100', 'detail' : 'XL 100.000', 'harga' : 98900}
paket_16 = {'kode_produk' : 'XX10GB', 'detail' : 'XL DATA 5 GB INTERNET + 5 GB YOUTUBE', 'harga' : 53450}
paket_17 = {'kode_produk' : 'XX20GB', 'detail' : 'XL DATA 10 GB INTERNET + 10 GB YOUTUBE', 'harga' : 80000}
paket_18 = {'kode_produk' : 'XX30GB', 'detail' : 'XL DATA 15 GB INTERNET + 15 GB YOUTUBE', 'harga' : 115300}
paket_19 = {'kode_produk' : 'XX40GB', 'detail' : 'XL DATA 20 GB INTERNET + 20 GB YOUTUBE', 'harga' : 159500}
paket_20 = {'kode_produk' : 'XX70GB', 'detail' : 'XL DATA 35 GB INTERNET + 35 GB YOUTUBE', 'harga' : 212500}

#TELOMSEL
paket_21 = {'kode_produk' : 'SN1', 'detail' : 'TSEL 1.000', 'harga' : 1850}
paket_22 = {'kode_produk' : 'SN5', 'detail' : 'TSEL 5.000', 'harga' : 5950}
paket_23 = {'kode_produk' : 'SN10', 'detail' : 'TSEL 10.000', 'harga' : 10400}
paket_24 = {'kode_produk' : 'SN25', 'detail' : 'TSEL 25.000', 'harga' : 20250}
paket_25 = {'kode_produk' : 'SN50', 'detail' : 'TSEL 50.000', 'harga' : 49300}
paket_26 = {'kode_produk' : 'SN100', 'detail' : 'TSEL 100.000', 'harga' : 97200}
paket_27 = {'kode_produk' : 'SD3GB', 'detail' : 'TSEL COMBO DATA 3 GB 1 BULAN', 'harga' : 65300}
paket_28 = {'kode_produk' : 'SD8GB', 'detail' : 'TSEL COMBO DATA 8 GB 1 BULAN', 'harga' : 92300}
paket_29 = {'kode_produk' : 'SD12GB', 'detail' : 'TSEL COMBO DATA 12 GB 1 BULAN', 'harga' : 105300}
paket_30 = {'kode_produk' : 'SD50GB', 'detail' : 'TSEL COMBO DATA 50 GB 1 BULAN', 'harga' : 210300}

#OVO
paket_31 = {'kode_produk' : 'OVO20', 'detail' : 'OVO 20K', 'harga' : 20800}
paket_32 = {'kode_produk' : 'OVO25', 'detail' : 'OVO 25K', 'harga' : 25800}
paket_33 = {'kode_produk' : '0VO50', 'detail' : 'OVO 50K', 'harga' : 60800}
paket_34 = {'kode_produk' : 'OVO75', 'detail' : 'OVO 75K', 'harga' : 75800}
paket_35 = {'kode_produk' : 'OVO100', 'detail' : 'OVO 100K', 'harga' : 100800}
paket_36 = {'kode_produk' : 'OVO150', 'detail' : 'OVO 150K', 'harga' : 150800}
paket_37 = {'kode_produk' : 'OVO200', 'detail' : 'OVO 200K', 'harga' : 200800}
paket_38 = {'kode_produk' : 'OVO300', 'detail' : 'OVO 300K', 'harga' : 300800}
paket_39 = {'kode_produk' : 'OVO400', 'detail' : 'OVO 400K', 'harga' : 400800}
paket_40 = {'kode_produk' : 'OVO500', 'detail' : 'OVO 500K', 'harga' : 500800}

#DANA
paket_41 = {'kode_produk' : 'DANA20', 'detail' : 'DANA 20K', 'harga' : 20800}
paket_42 = {'kode_produk' : 'DANA25', 'detail' : 'DANA 25K', 'harga' : 25800}
paket_43 = {'kode_produk' : 'DANA50', 'detail' : 'DANA 50K', 'harga' : 60800}
paket_44 = {'kode_produk' : 'DANA75', 'detail' : 'DANA 75K', 'harga' : 75800}
paket_45 = {'kode_produk' : 'DANA100', 'detail' : 'DANA 100K', 'harga' : 100800}
paket_46 = {'kode_produk' : 'DANA150', 'detail' : 'DANA 150K', 'harga' : 150800}
paket_47 = {'kode_produk' : 'DANA200', 'detail' : 'DANA 200K', 'harga' : 200800}
paket_48 = {'kode_produk' : 'DANA300', 'detail' : 'DANA 300K', 'harga' : 300800}
paket_49 = {'kode_produk' : 'DANA400', 'detail' : 'DANA 400K', 'harga' : 400800}
paket_50 = {'kode_produk' : 'DANA500', 'detail' : 'DANA 500K', 'harga' : 500800}

#PLN
paket_51 = {'kode_produk' : 'PLN20', 'detail' : 'PLN20K', 'harga' : 20200}
paket_52 = {'kode_produk' : 'PLN50', 'detail' : 'PLN50K', 'harga' : 50200}
paket_53 = {'kode_produk' : 'PLN100', 'detail' : 'PLN100K', 'harga' : 100200}
paket_54 = {'kode_produk' : 'PLN200', 'detail' : 'PLN200K', 'harga' : 200200}
paket_55 = {'kode_produk' : 'PLN500', 'detail' : 'PLN500K', 'harga' : 500200}
paket_56 = {'kode_produk' : 'PLN1JT', 'detail' : 'PLN1JT', 'harga' : 1000200}

#input database ke server redis
#input admin
ccell.hmset('admin_001', admin_001)
ccell.hmset('admin_002', admin_002)
ccell.hmset('admin_003', admin_003)
#input agen
ccell.hmset('agen_001', agen_001)
ccell.hmset('agen_002', agen_002)
ccell.hmset('agen_003', agen_003)
ccell.hmset('agen_004', agen_004)
ccell.hmset('agen_005', agen_005)
ccell.hmset('agen_006', agen_006)
ccell.hmset('agen_007', agen_007)
ccell.hmset('agen_008', agen_008)
ccell.hmset('agen_009', agen_009)
ccell.hmset('agen_010', agen_010)
#input paket
ccell.hmset('paket_1', paket_1)
ccell.hmset('paket_2', paket_2)
ccell.hmset('paket_3', paket_3)
ccell.hmset('paket_4', paket_4)
ccell.hmset('paket_5', paket_5)
ccell.hmset('paket_6', paket_6)
ccell.hmset('paket_7', paket_7)
ccell.hmset('paket_8', paket_8)
ccell.hmset('paket_9', paket_9)
ccell.hmset('paket_10', paket_10)
ccell.hmset('paket_11', paket_11)
ccell.hmset('paket_12', paket_12)
ccell.hmset('paket_13', paket_13)
ccell.hmset('paket_14', paket_14)
ccell.hmset('paket_15', paket_15)
ccell.hmset('paket_16', paket_16)
ccell.hmset('paket_17', paket_17)
ccell.hmset('paket_18', paket_18)
ccell.hmset('paket_19', paket_19)
ccell.hmset('paket_20', paket_20)
ccell.hmset('paket_21', paket_21)
ccell.hmset('paket_22', paket_22)
ccell.hmset('paket_23', paket_23)
ccell.hmset('paket_24', paket_24)
ccell.hmset('paket_25', paket_25)
ccell.hmset('paket_26', paket_26)
ccell.hmset('paket_27', paket_27)
ccell.hmset('paket_28', paket_28)
ccell.hmset('paket_29', paket_29)
ccell.hmset('paket_30', paket_30)
ccell.hmset('paket_31', paket_31)
ccell.hmset('paket_32', paket_32)
ccell.hmset('paket_33', paket_33)
ccell.hmset('paket_34', paket_34)
ccell.hmset('paket_35', paket_35)
ccell.hmset('paket_36', paket_36)
ccell.hmset('paket_37', paket_37)
ccell.hmset('paket_38', paket_38)
ccell.hmset('paket_39', paket_39)
ccell.hmset('paket_40', paket_40)
ccell.hmset('paket_41', paket_41)
ccell.hmset('paket_42', paket_42)
ccell.hmset('paket_43', paket_43)
ccell.hmset('paket_44', paket_44)
ccell.hmset('paket_45', paket_45)
ccell.hmset('paket_46', paket_46)
ccell.hmset('paket_47', paket_47)
ccell.hmset('paket_48', paket_48)
ccell.hmset('paket_49', paket_49)
ccell.hmset('paket_50', paket_50)
ccell.hmset('paket_51', paket_51)
ccell.hmset('paket_52', paket_52)
ccell.hmset('paket_53', paket_53)
ccell.hmset('paket_54', paket_54)
ccell.hmset('paket_55', paket_55)
ccell.hmset('paket_56', paket_56)










