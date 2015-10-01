# here's a motherfucking duck.
#
#           ,-.
#       ,--' ~.).
#     ,'         `.
#    ; (((__   __)))
#    ;  ( (#) ( (#)
#    |   \_/___\_/|
#   ,"  ,-'    `__".
#  (   ( ._   ____`.)--._        _
#   `._ `-.`-' \(`-'  _  `-. _,-' `-/`.
#    ,')   `.`._))  ,' `.   `.  ,','  ;
#  .'  .     `--'  /     ).   `.      ;
# ;     `-        /     '  )         ;
# \                       ')       ,'
#  \                     ,'       ;
#   \               `~~~'       ,'
#    `.                      _,'
#      `.                ,--'
#        `-._________,--'
#

import zlib
import base64
import random
import binascii

_DEFL_KEY = 0xdeadc0de	# default key
_DEFL_CMP = 6			# default compression level (0..9)

_FLAG_UTF8      = 0x01
_FLAG_UTF16     = 0x02
_FLAG_RFC1950   = 0x080000
_FLAG_RFC1951   = 0x100000

def gzinflate(code, base, size):
    return zlib.decompress(code[base: base + size], -15)

def gzdeflate(string, level):
    return zlib.compress(string, level)[2: -4]

def mb_detect_encoding(text, encoding_list = ['ascii']):
    for best in encoding_list:
        try:	unicode(text, best)
        except:	best = None
        else:	break
    return best

def mb_convert_encoding(str, src, dst):
    return str.decode(src).encode(dst)

# ========================================================================================== #
    
class base64x:

    _b64xl_xlat   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    _b64xl_xlat_a = 'abcdwxyzstuvrqponmijklefghABCDWXYZSTUVMNOPQRIJKLEFGH9876543210+/'
    _b64xl_xlat_b = '0123456789/abcdwxyzstuvrqponmijklefgh+ABCDWXYZSTUVMNOPQRIJKLEFGH'
    _b64xl_xlat_c = '0a1b2c3d4e5f6A7B8C9D/WXYZSTUVMNOPQRIJKLEFGH+wxyzstuvrqponmijklgh'

    _b64x_e_xlat = [0x30, 0x61, 0x31, 0x62, 0x32, 0x63, 0x33, 0x64, 0x34, 0x65, 0x35, 0x66, 0x36, 0x41, 0x37, 0x42,
                    0x38, 0x43, 0x39, 0x44, 0x2f, 0x57, 0x58, 0x59, 0x5a, 0x53, 0x54, 0x55, 0x56, 0x4d, 0x4e, 0x4f,
                    0x50, 0x51, 0x52, 0x49, 0x4a, 0x4b, 0x4c, 0x45, 0x46, 0x47, 0x48, 0x2b, 0x77, 0x78, 0x79, 0x7a,
                    0x73, 0x74, 0x75, 0x76, 0x72, 0x71, 0x70, 0x6f, 0x6e, 0x6d, 0x69, 0x6a, 0x6b, 0x6c, 0x67, 0x68] 
				          
    _b64x_d_xlat = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x2b, 0xff, 0xff, 0xff, 0x14,
                    0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0x0d, 0x0f, 0x11, 0x13, 0x27, 0x28, 0x29, 0x2a, 0x23, 0x24, 0x25, 0x26, 0x1d, 0x1e, 0x1f,
                    0x20, 0x21, 0x22, 0x19, 0x1a, 0x1b, 0x1c, 0x15, 0x16, 0x17, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0x01, 0x03, 0x05, 0x07, 0x09, 0x0b, 0x3e, 0x3f, 0x3a, 0x3b, 0x3c, 0x3d, 0x39, 0x38, 0x37,
                    0x36, 0x35, 0x34, 0x30, 0x31, 0x32, 0x33, 0x2c, 0x2d, 0x2e, 0x2f, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
                    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]

    def __init__(self, key):
        self.header = []
        self.buffer = ""
        self.state = (key & 0xffffffff)

    def _shr_32(self, x, n):
        y = ((x & 0x7fffffff) >> n)
        if (0x80000000 & x):
            return (y | (1 << (31-n)))
        return y

    def _shl_32(self, x, n):
        if (n):
            mask = (1 << (32-n)) - 1
            x = ((x & mask) << n)
        return x & 0xffffffff
        
    def _add_32(self, x, y):
        return (x + y) & 0xffffffff
     
    def _rol_32(self, x, n):
        if (n > 0):
            return self._shl_32(x, n) | self._shr_32(x, 32 - n)
        return self._shl_32(x, n)

    def b64xenc(self, value):     
        result = (value + self.state) & 0x3f
        self.state = self._rol_32(self.state + 0x4242, value & 0x7)
        self.state = self.state ^ value
        return result

    def b64xdec(self, value):
        value = (value - self.state) & 0x3f
        self.state = self._rol_32(self.state + 0x4242, value & 0x7)
        self.state = self.state ^ value
        return value
        
    def xform(self, value, src, dst):
        result = ''
        for n in range(0, len(value)):
            if (value[n] != '='):
                result += dst[src.index(value[n])]
        return result

    def encode_triple(self, a, b, c, size):
        self.buffer +=                chr( self._b64x_e_xlat[self.b64xenc(((a & 0xfc) >> 2))] )
        self.buffer +=                chr( self._b64x_e_xlat[self.b64xenc(((a & 0x03) << 4) + ((b & 0xf0) >> 4))] )
        if (size > 1): self.buffer += chr( self._b64x_e_xlat[self.b64xenc(((b & 0x0f) << 2) + ((c & 0xc0) >> 6))] )
        if (size > 2): self.buffer += chr( self._b64x_e_xlat[self.b64xenc(((c & 0x3f)))] )

    def encode_buffer(self, code, size) :
        ix = 0    
        while (size > 0):
            if (size == 1): return self.encode_triple(ord(code[ix]), 0, 0, 1)
            if (size == 2): return self.encode_triple(ord(code[ix]), ord(code[ix + 1]), 0, 2)
            self.encode_triple(ord(code[ix]), ord(code[ix + 1]), ord(code[ix + 2]), 3)
            ix += 3
            size -= 3    
            
    def encode_header(self, csum, bits, size):
        if size > 0: # UTF8, RFC1951
            bits = bits | _FLAG_RFC1951
        else: 
            bits = bits | 0
            
        self.encode_triple(self._shr_32(bits,  0) & 0xff, self._shr_32(bits,  8) & 0xff, self._shr_32(bits, 16) & 0xff, 3)
        self.encode_triple(self._shr_32(bits, 24) & 0xff, self._shr_32(csum,  0) & 0xff, self._shr_32(csum,  8) & 0xff, 3)
        self.encode_triple(self._shr_32(csum, 16) & 0xff, self._shr_32(csum, 24) & 0xff, self._shr_32(size,  0) & 0xff, 3)
        self.encode_triple(self._shr_32(size,  8) & 0xff, self._shr_32(size, 16) & 0xff, self._shr_32(size, 24) & 0xff, 3)
        
    def encode64x(self, code, encoding, compress):
        self.buffer += chr( self._b64x_e_xlat[self.b64xenc(random.randint(0, 0x3f) & 0x3f)] )
        self.buffer += chr( self._b64x_e_xlat[self.b64xenc(random.randint(0, 0x3f) & 0x3f)] )
        self.state = (self._rol_32(self.state, 16) ^ self.state) & 0xffffffff

        uncompressed = 0
        compress = max(0, min(9, compress))
        if (compress > 0): # RFC1951 deflate compression
            comp = gzdeflate(code, compress)
            if (comp != False and len(comp) < len(code)): 
                uncompressed = len(code) # use compression only when result is smaller than input
                code = comp

        self.encode_header(binascii.crc32(code) & 0xffffffff, encoding, uncompressed)
        self.encode_buffer(code, len(code))
        return self.buffer
    
    def decode_buffer(self, code, base, size):
        tmp = [0, 0, 0, 0]
        ix = base
        phase = 0
        
        while (ix < size):
            lix = ix
            ix += 1
            d = self._b64x_d_xlat[ord( code[lix] )]
            if (d != 0xff): # skip garbage characters
                d = self.b64xdec(d)
                if (len(self.header) < 16):
                    self.header.append(d)
                    continue
    
                phase = phase & 0x03
                tmp[phase] = d
                phase += 1
                if (4 != phase): 
                    if (lix + 1 < size): continue
                    tmp[phase] = 0
                
                if (phase > 1): self.buffer += chr( ((tmp[0]       ) << 2) + ((tmp[1] & 0x30) >> 4) )
                if (phase > 2): self.buffer += chr( ((tmp[1] & 0x0f) << 4) + ((tmp[2] & 0x3c) >> 2) )
                if (phase > 3): self.buffer += chr( ((tmp[2] & 0x03) << 6) + ((tmp[3]       )     ) )

        return (16 == len(self.header))
        
    def decode_header_byte(self, byte):
        base = int(byte * 4 / 3)
        exp = byte % 0x03

        if (exp == 0x00): return ((self.header[base + 0]       ) << 2) + ((self.header[base + 1] & 0x30) >> 4)
        if (exp == 0x01): return ((self.header[base + 0] & 0x0f) << 4) + ((self.header[base + 1] & 0x3c) >> 2)
        if (exp == 0x02): return ((self.header[base + 0] & 0x03) << 6) + ((self.header[base + 1]       )     )
        
    def decode_header_word(self, base):
        return \
			self._shl_32(self.decode_header_byte(base + 0),  0) | \
			self._shl_32(self.decode_header_byte(base + 1),  8) | \
			self._shl_32(self.decode_header_byte(base + 2), 16) | \
			self._shl_32(self.decode_header_byte(base + 3), 24) 
    
    def decode64x(self, code):    
        codesize = len(code)
        if (codesize < (2 + 4*4)):
            return False # 2-byte seed, 16-byte header.

        seed0 = self._b64x_d_xlat[ord( code[0] )]
        seed1 = self._b64x_d_xlat[ord( code[1] )]
        if (seed0 > 0x3f or seed1 > 0x3f):
            return False # bad input

        self.b64xdec(seed0)
        self.b64xdec(seed1)
        self.state ^= self._rol_32(self.state, 16)
        self.state = self.state & 0xffffffff

        if (not self.decode_buffer(code, 2, codesize)):
            return False

        bits = self.decode_header_word(0)
        csum = self.decode_header_word(4)
        size = self.decode_header_word(8)
        data = self.buffer

        if (csum != 0): 
            if (csum != (binascii.crc32(data) & 0xffffffff)):
                return False

        if (0 != (bits & _FLAG_RFC1950)):
            data = gzinflate(data, 2, len(data) - 6)

        if (0 != (bits & _FLAG_RFC1951)): 
            data = gzinflate(data, 0, len(data))        

        if (data == False):
            return false
        if (0 != (bits & (_FLAG_RFC1950|_FLAG_RFC1951)) and size != len(data)):
            return False        

        return data
    
# ========================================================================================== #
# == public api ============================================================================ #

#  input (type): "UTF-8", "UTF-16", "ASCII" result: UTF-8/ASCII or False
def encode_any(code, type = False, compress = _DEFL_CMP, key = _DEFL_KEY):
    x = base64x(key)
    if (type == False):
        type = mb_detect_encoding(code, "ASCII, UTF-8, UTF-16")
    if (type == "ASCII" or type == "UTF-8") :
        return x.encode64x(code, _FLAG_UTF8, compress)
    if (type == "UTF-16") :
        return x.encode64x(mb_convert_encoding(code, "UTF-8", type), _FLAG_UTF16, compress)
    # assume raw binary data
    return x.encode64x(code, 0, compress)

# input: UTF-8/ASCII result: UTF-8/ASCII or False
def encode(code, compress = _DEFL_CMP, key = _DEFL_KEY):
    x = base64x(key)
    return x.encode64x(code, _FLAG_UTF8, compress)

# input: UTF-8/ASCII result: UTF-8/binary or False
def decode(code, key = _DEFL_KEY):
    x = base64x(key)
    if (code != False):
        return x.decode64x(code)
    return False

# input: binary result: UTF-8/ASCII or False
def encodexl(code, xlat):
    x = base64x(0)
    return x.xform(base64.b64encode(code), base64x._b64xl_xlat, xlat)

# input: UTF-8/ASCII result: binary or False
def decodexl(code, xlat):
    x = base64x(0)
    if (code != False):
        tmp = x.xform(code, xlat, base64x._b64xl_xlat)
        while ((len(tmp) & 3) > 0):
            tmp += '='
        return base64.b64decode(tmp)
    return False

# ========================================================================================== #
# == test code ============================================================================= #
    
if __name__ == '__main__':

    # legacy support
    print decodexl(encodexl('shitcock', base64x._b64xl_xlat_a), base64x._b64xl_xlat_a)

    # create highly-compressible string
    str = 'shitcock-motherfucking-cock-cock-turbo!-cocksucker-cock-cocksucker-cock-shit-cock-cocksucker-cock-cock-cock-cock-cock-cock-cock-cock-cock-cock-shit-cock-shitcock-ticktock'
    str += str
    str += str
    str += str

    xxx = encode(str)
    print xxx

    yyy = decode(xxx)
    print yyy