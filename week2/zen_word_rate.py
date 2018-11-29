import this
import codecs
import operator

raw_zen = this.s.encode().decode()
zen = codecs.decode(raw_zen, 'rot13')
zen_map = dict()
zen_list = list()

for word in zen.split():
    cleaned_word = word.strip('.,!-').lower()
    if cleaned_word in zen_map:
        zen_map[cleaned_word] +=1
    else:
        zen_map[cleaned_word] =  1
'''
for k,v in zen_map.items():
    zen_list.append((v,k))

zen_list.sort(reverse=True)
print(zen_list[:3])

for i in zen_list[:3]:
    print(i[1], i[0])
'''

word_count_items = sorted(
    zen_items, key=operator.itemgetter(1), reverse=True
)

print(word_count_items[:3])
