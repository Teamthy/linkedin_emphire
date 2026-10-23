PHP just gave the whole industry a lesson.

Two critical, unauthenticated remote code execution bugs in the PHP core. CVE-2026-109618 and CVE-2026-109619, both CVSS 9.2. Not in a plugin, not in a framework. In the runtime. PHP runs on about 70 percent of the web.

The exploit is reached while PHP parses the request. Before any application code runs. Your input validation, your framework, your WAF rules: none of them get a turn. The layer that is supposed to defend you had not even started yet.

So you cannot patch this in your code. The fix is in the runtime: 8.2.35, 8.3.36, 8.4.27, 8.5.12. And there is no official release for 8.1 and below. If you are on 8.1, the answer is a backport and a conversation with whoever owns the server.

The discovery story is the other lesson. Calif found it with GPT-5.6 Sol. Wiz found it independently. Agents that read code this deep are now how these bugs get found.

And the honest part:

Amazon logged an attempt about four days before the patch. Cloudflare is counting millions of attempts. Exploit tooling is public. There is no confirmed breach, and CISA has not KEV-listed either CVE. On a stock install the public exploit does not work out of the box.

That is what the check is for. The one check that has never failed is the one that runs before your users get to find it.

Your check has to reach the layer you do not own.

Break it before your users do, or their relatives do.

#PHP2Shell #cybersecurity #AIsecurity #redteaming
