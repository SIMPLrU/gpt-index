"""Query map."""

from typing import Type

from gpt_index.data_structs.struct_type import IndexStructType
from gpt_index.indices.query.base import BaseGPTIndexQuery
from gpt_index.indices.query.keyword_table.query import (
    GPTKeywordTableGPTQuery,
    GPTKeywordTableRAKEQuery,
    GPTKeywordTableSimpleQuery,
)
from gpt_index.indices.query.list.embedding_query import GPTListIndexEmbeddingQuery
from gpt_index.indices.query.list.query import GPTListIndexQuery
from gpt_index.indices.query.schema import QueryMode
from gpt_index.indices.query.tree.embedding_query import GPTTreeIndexEmbeddingQuery
from gpt_index.indices.query.tree.leaf_query import GPTTreeIndexLeafQuery
from gpt_index.indices.query.tree.retrieve_query import GPTTreeIndexRetQuery
from gpt_index.indices.query.tree.summarize_query import GPTTreeIndexSummarizeQuery
from gpt_index.indices.query.vector_store.faiss import GPTFaissIndexQuery
from gpt_index.indices.query.vector_store.simple import GPTSimpleVectorIndexQuery
from gpt_index.indices.query.vector_store.weaviate import GPTWeaviateIndexQuery

MODE_TO_QUERY_MAP_TREE = {
    QueryMode.DEFAULT: GPTTreeIndexLeafQuery,
    QueryMode.RETRIEVE: GPTTreeIndexRetQuery,
    QueryMode.EMBEDDING: GPTTreeIndexEmbeddingQuery,
    QueryMode.SUMMARIZE: GPTTreeIndexSummarizeQuery,
}

MODE_TO_QUERY_MAP_LIST = {
    QueryMode.DEFAULT: GPTListIndexQuery,
    QueryMode.EMBEDDING: GPTListIndexEmbeddingQuery,
}

MODE_TO_QUERY_MAP_KEYWORD_TABLE = {
    QueryMode.DEFAULT: GPTKeywordTableGPTQuery,
    QueryMode.SIMPLE: GPTKeywordTableSimpleQuery,
    QueryMode.RAKE: GPTKeywordTableRAKEQuery,
}


# vector-based indices
MODE_TO_QUERY_MAP_FAISS = {
    QueryMode.DEFAULT: GPTFaissIndexQuery,
}

MODE_TO_QUERY_MAP_SIMPLE = {
    QueryMode.DEFAULT: GPTSimpleVectorIndexQuery,
}

MODE_TO_QUERY_MAP_WEAVIATE = {
    QueryMode.DEFAULT: GPTWeaviateIndexQuery,
}


def get_query_cls(
    index_struct_type: IndexStructType, mode: QueryMode
) -> Type[BaseGPTIndexQuery]:
    """Get query class."""
    if index_struct_type == IndexStructType.TREE:
        return MODE_TO_QUERY_MAP_TREE[mode]
    elif index_struct_type == IndexStructType.LIST:
        return MODE_TO_QUERY_MAP_LIST[mode]
    elif index_struct_type == IndexStructType.KEYWORD_TABLE:
        return MODE_TO_QUERY_MAP_KEYWORD_TABLE[mode]
    elif index_struct_type == IndexStructType.DICT:
        return MODE_TO_QUERY_MAP_FAISS[mode]
    elif index_struct_type == IndexStructType.SIMPLE_DICT:
        return MODE_TO_QUERY_MAP_SIMPLE[mode]
    elif index_struct_type == IndexStructType.WEAVIATE:
        return MODE_TO_QUERY_MAP_WEAVIATE[mode]
    else:
        raise ValueError(f"Invalid index_struct_type: {index_struct_type}")
