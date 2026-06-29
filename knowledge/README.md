# knowledge/ — provider-neutral "second brain" index

The recall layer for Bob. **NOT Vertex** (that was v1). Backend is local / pgvector /
LlamaIndex — chosen and built under **epic E3** (knowledge index + `knowledge_search` tool)
and grown under **epic E7** (cross-repo aggregation, two-way memory with value-semantics).

Two-way memory facts are immutable values (subject / content_hash / asserted_at /
asserted_by / supersedes; scope mandatory; conflict-policy declared) — signing does not fix
recall corruption, so the conflict policy is explicit (P10, per Hickey/Kleppmann).
