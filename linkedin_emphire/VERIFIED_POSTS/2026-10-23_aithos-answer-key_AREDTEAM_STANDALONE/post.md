Most AI safety evals have an answer key, and the answer key is the quietest part of the stack.

You can hide a value system in a benchmark and it will look like a measurement. The model is tested, the score is reported, and nobody notices the test itself took a side.

Aithos Research Foundation is working on this problem, and their recent work makes it concrete. One paper tests whether frontier models meet the structural prerequisites for coherent moral behavior, across nine models and three simulated deployments. The result: none of them does, consistently. Their LARA work has three AI judges score model outputs against verbatim legal text; across twelve models, compliance lands between 7 and 54 percent.

The number that matters to me is not the compliance rate. It is what the method refuses to do: assume a single correct moral answer. Their standard is a floor: the competence a system shows before it is allowed to act, not a target you maximize.

I see the same failure from the other side of the stack. In red teaming, the model is rarely the weak point. The pass definition is. A check nobody can see, contest, or re-run is not a safety result. It is a private opinion with a number on it.

In a pluralistic world, the eval worth shipping tests competence, not conformity: can the system hold its reasoning to scrutiny, can it preserve a person's ability to say no, can anyone re-run it and see the same pass.

Move the check out of the private lab, and the number you ship stops being a guess.
