import binascii # used to go from strings to hex
import hashlib #hashing library

def string_to_hex(s):
	S = bytes(s, 'utf-8')
	S = binascii.hexlify(S)
	return str(S, 'ascii')

def hex_to_string(h):
	H = bytes(h, 'utf-8')
	H = binascii.unhexlify(H)
	return str(H, 'ascii')

#Convert standard base 10 integer to a base determined by an alphabet
def dec_to(n, alphabet):
	N = n
	s = ''
	while N > 0:
		digit = N % len(alphabet)
		digit_char = alphabet[digit]
		s = digit_char + s
		N //= len(alphabet)
	return s   

def dec_to_hex(dec):
	numb = dec
	alphabet = '0123456789abcdef'
	h_string = dec_to(numb, alphabet)
	return h_string 

## From Destiner/blocksmith    
def hex_to_b58(address_hex):
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    # Get the number of leading zeros 
    leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
    # Convert hex to decimal
    address_int = int(address_hex, 16)
    # Convert decimal to base58
    b58_string = dec_to(address_int, alphabet)
    # Add '1' for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = '1' + b58_string
    return b58_string

def b58_to_dec(base58_string):
	alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	numb = 0
	# Convert to decimal (base 10)
	for i in range(len(base58_string)):
		coeff = alphabet.index(base58_string[-(i+1)])
		numb += coeff * 58 ** i
	return numb

def b58_to_hex(b58_string):
	b58_dec = b58_to_dec(b58_string)
	return dec_to_hex(b58_dec)

def hex_to_b58c(h):
	
	# Must pass bytes object to hashlib.sha256
	hex_hash1 = hashlib.sha256(bytes.fromhex(h)).digest()
	hex_hash2 = hashlib.sha256(hex_hash1).hexdigest()
	hex_hash_c = h + hex_hash2[0:8]
	return hex_to_b58(hex_hash_c)

# Convert base58check to hex without checksum
def b58c_to_hex(b58c):
	h = b58_to_hex(b58c)
	h = h[0:len(h) - 8]
	return h

# Convert message to address
def mess_to_add(message, padding = '0', pre = '6F'):
	M_hex = string_to_hex(message)
	## Specific to BTC where addresses are 160 bit
	# max length of message
	if len(M_hex) > 40:
		print("Message too long (x characters), must be 20 characters max")
		return
	if len(M_hex) < 40:
		zeros = 40 - len(M_hex)
		M_hex = zeros * padding + M_hex
	
	# add version
	M_hex = pre + M_hex
	# write in base58check
	M_b58c = hex_to_b58c(M_hex)
	return M_b58c

# Convert address to message
def add_to_mess(address):
	# convert to hex and remove checksum
	add_hex = b58c_to_hex(address)
	# remove version
	mess_hex = add_hex[2:len(add_hex)]
	# convert hex to string
	return hex_to_string(mess_hex)

# Tests
if __name__ == '__main__':
	print(string_to_hex('P+V'))
	print(add_to_mess(mess_to_add('P+V')))
	print(mess_to_add('P+V'))	
	print(b58c_to_hex(mess_to_add('P+V')))	
	#print("hello".encode("hex"))

   