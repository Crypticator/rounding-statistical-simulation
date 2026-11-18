# Author checks — complete draft v0.6

Date: 17 November 2026. These checks support delivery and do not confer independent final approval.

## Scope and source fidelity

The source approved in v0.5.1 was reconstructed and its SHA-256 matched the reviewer record (`faa0065e343f728394a4841b82b8c967f8b6eb9ad4ca54c05c8255c3a94c6406`). The three reviewer corrections were applied to the submitted programs and their hashes matched the corrected evidence. The source text of sections 1.1–1.7, Chapters 2–10, Appendices A–D, the abstract and references is unchanged, after ignoring surrounding whitespace. New text consists of section 1.8, Chapter 11 and Appendix E; front matter and the contents were updated.

The new synthesis was checked against the complete theorem statements, particularly the uniform prior, even cell length, restricted group action, retained coordinates, acceptance rate, and offline model. A mechanical existence check resolved 31 distinct section references and ten distinct numbered-result references in the additions. This checks existence, not logical correctness of every reference; the final review must assess the synthesis independently.

## Scientific computations

Only the corrected `scripts/verify_two_worlds.py` was rerun for this consolidation. It passed 28 domains, 44,160 elementary tuples, 217 weighted objectives, 1,104 exact tie rows and 836 numerical row optimizations. Maximum objective discrepancy was below 1e-16 and maximum constraint residual below 2.3e-16. The four measured example values are 77/416, 5/64, 1/104 and 73/832. Its JSON output is byte-identical to both the previously recorded data and the reviewer's corrected run.

A content comparison of all earlier scientific programs and data found only the intended corrected two-world verifier different from v0.5. Other campaigns were not rerun because the synthesis changes neither their mathematical inputs nor their programs. Their existing results remain evidence from earlier runs, not newly executed experiments. Numerical optimizations corroborate exact calculations and are not symbolic certificates.

## Export and inspection

The final PDF has 85 pages, eleven chapters and five appendices. The DOCX has 1,945 native mathematical objects, fourteen positive-part subscripts and 32 explicitly double-struck symbols. The strengthened document guard passed without issues.

Content regions on 72 retained pages were compared with a current-engine rendering of the corrected approved DOCX. Seventy-one were pixel-identical. The references page differs in vertical placement, but its extracted content is identical and direct visual inspection confirms all eleven entries remain complete and readable. Headers and footers were excluded from this pixel comparison.

Pages 1, 3, 7, 66–71 and 81–85 were directly inspected. The additions, equations, notation tables, repeated headers, margins and page boundaries are readable, with no clipping observed. Appendix E spans pages 81–84; Chapter 11 spans pages 66–71. The LaTeX export is auxiliary and was not compiled. PDF pagination and bytes may differ across rendering engines.

## Review status

Parts I–IV retain their scoped approvals. The new synthesis, notation appendix and complete-volume coherence await the final independent review. No universal priority claim, formal certification, academic degree or cryptographic security claim follows from these author checks.
