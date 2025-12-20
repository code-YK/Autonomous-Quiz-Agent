---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	extract(extract)
	organize(organize)
	generate(generate)
	rank(rank)
	validate(validate)
	__end__([<p>__end__</p>]):::last
	__start__ --> extract;
	extract --> organize;
	generate --> rank;
	organize --> generate;
	rank --> validate;
	validate --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
