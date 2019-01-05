class Solution(object):
    def subdomainVisits(self, cpdomains):
        sitem = list()
        new_dic = {}

        for item in cpdomains:
            sitem.append(item.split(' '))
        # print(sitem)
        for i in range(len(sitem)):
            combine = ''
            num_item = int(sitem[i][0])
            item_detail = sitem[i][1].split('.')
            # print(item_detail)
            # for word in item_detail:
            #     if word not in new_dic.keys():
            #         new_dic[word] = num_item
            #     else:
            #         new_dic[word] += num_item
            for i in range(len(item_detail)-1,-1,-1):
                # print('combine',combine)
                
                if i == len(item_detail)-1:
                    combine = item_detail[i]
                                        
                    if combine not in new_dic.keys():
                        new_dic[combine] = num_item
                    else:
                        new_dic[combine] += num_item
                    # print item_detail[i]
                else:
                    combine = item_detail[i] + '.' + combine
                    
                    if combine not in new_dic.keys():
                        new_dic[combine] = num_item
                    else:
                        new_dic[combine] += num_item

#             print new_dic
#             print(num_item, item_detail)
            # print(new_dic)
            result = []
            for i in new_dic.keys():
                result.append(str(new_dic[i])+' ' + i)
                # print(i,j)
                
            # print result
        return result
        # print sitem
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        