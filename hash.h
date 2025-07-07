#ifndef __HASH_H__
#define __HASH_H__

#include "initialize.h"

void alloc_assert(void *p, char *s);


typedef struct buffer_info_Hash {
    unsigned long read_hit;                      /*�����hit����ʾsector�����д�������û���еĴ���*/
    unsigned long read_miss_hit;
    unsigned long write_hit;
    unsigned long write_miss_hit;
    unsigned long write_free;
    unsigned long eject;

    struct buffer_group *buffer_head;            /*as LRU head which is most recently used*/
    struct buffer_group *buffer_tail;            /*as LRU tail which is least recently used*/
    struct _HASH_NODE_ **nodeArray;
    unsigned int current_limit;
    unsigned int max_buffer_page;
    unsigned int current_buffer_page;

    unsigned int count;                         /*AVL����Ľڵ�����*/
    int (*keyCompare)(struct _HASH_NODE_ *, struct _HASH_NODE_ *);

    int (*free)(struct _HASH_NODE_ *);
} tHash;


tHash *hash_create(int *freeFunc);

int hash_add(tHash *pHash, struct _HASH_NODE_ *pInsertNode);

struct _HASH_NODE_ *hash_find(tHash *pHash, struct _HASH_NODE_ *pKeyNode);

int hash_del(tHash *pHash, struct _HASH_NODE_ *pDelNode);

void hash_node_free(tHash *pHash, struct _HASH_NODE_ *pNode);

int hash_destroy(tHash *pHash);


#endif