#include <stdio.h>
#include <stdlib.h>

#include "hash.h"


#define HASH_CELL_NUM 3

tHash *hash_create(int *freeFunc){
	tHash *pHash = NULL;

	if(!freeFunc)
		return NULL;

	pHash = (tHash *)malloc(sizeof(tHash));
	
	if(pHash != NULL)
	{
		memset((void *)pHash , 0 , sizeof(tHash));
		pHash->free = (void *)freeFunc;
		pHash->nodeArray = NULL;
	}

	return pHash;
}

//
int hash_add(tHash *pHash ,  HASH_NODE *pInsertNode){
	int growthFlag=0 , ret = 0;
	unsigned long long i = 0;
	if(!pHash || !pInsertNode)
		return 0;

	if(pHash->nodeArray == NULL){
		unsigned long long hash_len = ((pHash->max_buffer_page + HASH_CELL_NUM - 1) / HASH_CELL_NUM);//向上取整--确保所有缓存页都能被正确处理
		pHash->nodeArray = malloc(sizeof(HASH_NODE) * hash_len);
		alloc_assert(pHash->nodeArray, "pHash->nodeArray");		
		for(; i < hash_len; ++i){
			pHash->nodeArray[i] = NULL;
		}
	}

	buf_node* node = (buf_node*)pInsertNode;

	i = node->group % pHash->max_buffer_page;//计算哈希索引
	i = i / 3;//分散哈希冲突

	pInsertNode->next = pHash->nodeArray[i];    //头插法
	pHash->nodeArray[i] = pInsertNode;
	
	pHash->count++;
	return ret;
}


HASH_NODE *hash_find(tHash *pHash, HASH_NODE *pKeyNode){
	if(!pHash || !pHash->count || !pHash->nodeArray)
		return NULL;
	unsigned long long pos = 0;
	buf_node* node = (buf_node*)pKeyNode;
	HASH_NODE *interNode;
	unsigned int target = node->group;
	HASH_NODE *preNode = NULL;
		
	pos = node->group % pHash->max_buffer_page; //max变了，导致pos越界，从而导致访问非法内存---段错误
	pos /= 3;                                   //算具体落在哪个桶内
	interNode = pHash->nodeArray[pos];          //再从这个桶的头部开始查找
	
	while(interNode){
		node = (buf_node*)interNode;
		if(node->group == target)
			break;
		preNode = interNode;
		interNode = interNode->next;
	}
	if(interNode){
		if(preNode){
			preNode->next = interNode->next;
			interNode->next = pHash->nodeArray[pos];
			pHash->nodeArray[pos] = interNode;
		}
		return interNode;
	}
	
	return NULL;
}

int hash_del(tHash *pHash ,HASH_NODE *pDelNode){
	int ret = 0;
	
	unsigned long long pos = 0;
	buf_node* node = (buf_node*)pDelNode;
	HASH_NODE *interNode;
    //HASH_NODE *Rnode;
	unsigned int target = node->group;
	HASH_NODE *preNode = NULL;
	
	pos = node->group % pHash->max_buffer_page;
	pos /= 3;
	interNode = pHash->nodeArray[pos];

    while(interNode){
		node = (buf_node*)interNode;
//        if(target==45423)
//            break;
        //printf("Checking node: %p, group: %u\n", interNode, node->group); // 打印当前节点的 group 值

		if(node->group == target)
			break;
		preNode = interNode;
		interNode = interNode->next;
	}
	
	if(interNode){
		if(preNode){
			preNode->next = interNode->next;
		}else{
			pHash->nodeArray[pos] = interNode->next;
		}
		pHash->count--;
	}
	
	return 0;
}

void hash_node_free(tHash *pHash, HASH_NODE *pNode){
	if(!pHash || !pNode)
		return;
	free(((struct buffer_group *)pNode)->accessCount);
	free(((struct buffer_group *)pNode)->accessTime);
	(pHash->free)(pNode);
	return ;
}



int hash_destroy(tHash *pHash){
	HASH_NODE *pNode = NULL;
	if(!pHash)
		return 0;

	unsigned long long hash_len = ((pHash->max_buffer_page + HASH_CELL_NUM - 1) / HASH_CELL_NUM);//HASH_CELL_NUM---每个桶的容量上限
	int i = 0;
	
	for(;i < hash_len; ++i){
		pNode = pHash->nodeArray[i];
		while(pNode){
			HASH_NODE *willFree = pNode;
			pNode = pNode->next;
			free(willFree);
		}
	}

	free(pHash->nodeArray);//释放哈希桶数组
	free(pHash);
	
	return 0;
}


