PHP just shipped an emergency patch for two 9.2 remote code execution bugs it calls PHP2Shell (CVE-2026-109618 and CVE-2026-109619). The line that should unsettle anyone who runs PHP: the flaw is reached while PHP is parsing your request, before a line of your application code runs.

That is the hard part. Everything you spend your security budget on in your own layer, input validation, the framework, the auth, is not where this lives. You cannot patch it in your code. The only fix is the runtime: 8.2.35, 8.3.36, 8.4.27, 8.5.12. On 8.1 or older, there is no official release at all.

Worth pausing on: a researcher used an AI model to help find it, and Wiz found it independently, in a language on roughly 70% of the web. The layer we least control is where the interesting bugs are, and a model helped find one there.

Keep it honest, though. Attempt signals are already out: Amazon logged one days before the patch, Cloudflare is counting millions of attempts, exploit tooling is public. But there is no confirmed breach, CISA has not listed it as known-exploited, and the public exploits reportedly do not work on a default install. Patch now, because the window between attempted and confirmed is the dangerous one.

The red team lesson: your check has to reach the layer you do not own. Know what runtime your stack runs, verify the patch held, do it before the scanners do. Break it before your users, or their relatives, do.

#PHP2Shell #cybersecurity #AIsecurity #redteaming
