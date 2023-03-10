"""Subclasses from base prompt."""
from typing import List

from gpt_index.prompts.base import Prompt
from gpt_index.prompts.prompt_type import PromptType


class SummaryPrompt(Prompt):
    """Summary prompt.

    Prompt to summarize the provided `context_str`.

    Required template variables: `context_str`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.SUMMARY
    input_variables: List[str] = ["context_str"]


class TreeInsertPrompt(Prompt):
    """Tree Insert prompt.

    Prompt to insert a new chunk of text `new_chunk_text` into the tree index.
    More specifically, this prompt has the LLM select the relevant candidate
    child node to continue tree traversal.

    Required template variables: `num_chunks`, `context_list`, `new_chunk_text`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.TREE_INSERT
    input_variables: List[str] = ["num_chunks", "context_list", "new_chunk_text"]


class TreeSelectPrompt(Prompt):
    """Tree select prompt.

    Prompt to select a candidate child node out of all child nodes
    provided in `context_list`, given a query `query_str`. `num_chunks` is
    the number of child nodes in `context_list`.

    Required template variables: `num_chunks`, `context_list`, `query_str`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.TREE_SELECT
    input_variables: List[str] = ["num_chunks", "context_list", "query_str"]


class TreeSelectMultiplePrompt(Prompt):
    """Tree select multiple prompt.

    Prompt to select multiple candidate child nodes out of all
    child nodes provided in `context_list`, given a query `query_str`.
    `branching_factor` refers to the number of child nodes to select, and
    `num_chunks` is the number of child nodes in `context_list`.

    Required template variables: `num_chunks`, `context_list`, `query_str`,
        `branching_factor`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type = PromptType.TREE_SELECT_MULTIPLE
    input_variables: List[str] = [
        "num_chunks",
        "context_list",
        "query_str",
        "branching_factor",
    ]


class RefinePrompt(Prompt):
    """Refine prompt.

    Prompt to refine an existing answer `existing_answer` given a context `context_msg`,
    and a query `query_str`.

    Required template variables: `query_str`, `existing_answer`, `context_msg`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.REFINE
    input_variables: List[str] = ["query_str", "existing_answer", "context_msg"]


class QuestionAnswerPrompt(Prompt):
    """Question Answer prompt.

    Prompt to answer a question `query_str` given a context `context_str`.

    Required template variables: `context_str`, `query_str`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.QUESTION_ANSWER
    input_variables: List[str] = ["context_str", "query_str"]


class KeywordExtractPrompt(Prompt):
    """Keyword extract prompt.

    Prompt to extract keywords from a text `text` with a maximum of
    `max_keywords` keywords.

    Required template variables: `text`, `max_keywords`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.KEYWORD_EXTRACT
    input_variables: List[str] = ["text", "max_keywords"]


class QueryKeywordExtractPrompt(Prompt):
    """Query keyword extract prompt.

    Prompt to extract keywords from a query `query_str` with a maximum
    of `max_keywords` keywords.

    Required template variables: `query_str`, `max_keywords`

    Args:
        template (str): Template for the prompt.
        **prompt_kwargs: Keyword arguments for the prompt.

    """

    prompt_type: PromptType = PromptType.QUERY_KEYWORD_EXTRACT
    input_variables: List[str] = ["question", "max_keywords"]
