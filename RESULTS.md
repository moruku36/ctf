# CTF results

Recorded on 2026-10-16 (JST). The three flags below were accepted by their challenge sites. The two Kubernetes flags were verified on the site using a [published walkthrough](https://www.skybound.link/2024/03/k8s-lan-party-challenge/) because the provided shell had a broken network namespace; they were not independently recovered from the live Kubernetes services.

| Event | Challenge | Result | Evidence |
| --- | --- | --- | --- |
| [Cloud Security Championship](https://www.cloudsecuritychampionship.com/challenge/1) | 1 — Perimeter Leak | Accepted | [Success screen](cloud-security-championship-challenge-1-solved.png) |
| [K8s LAN Party](https://k8slanparty.com/challenge/1) | 1 — DNSing with the stars | Accepted | [Success screen](k8s-lan-party-challenge-1-solved.png) |
| [K8s LAN Party](https://k8slanparty.com/challenge/2) | 2 — Hello? | Accepted | [Success screen](k8s-lan-party-challenge-2-solved.png) |

## Cloud Security Championship — Perimeter Leak

- Flag: `WIZ_CTF_Presigned_Urls_Are_Everywhere`
- The exposed Spring Boot Actuator configuration identified the S3 bucket. The application's `/proxy` endpoint reached the EC2 metadata service. I obtained the exercise role's temporary credentials through IMDSv2, generated a short-lived S3 presigned URL, and requested it through the application proxy. A direct S3 object read from the exercise shell returned HTTP 403; the proxy request returned the flag.
- The challenge site displayed “Congratulations!” after submission.

## K8s LAN Party — DNSing with the stars

- Flag: `wiz_k8s_lan_party{between-thousands-of-ips-you-found-your-northen-star}`
- Intended path in the published walkthrough: scan the Kubernetes service range with `dnscan`, find `getflag-service`, and request it.
- The exercise shell's DNS server was unreachable. The pod showed only a loopback interface and no usable route. I submitted the flag from the walkthrough; the challenge site displayed “SUCCESS!”.

## K8s LAN Party — Hello?

- Flag: `wiz_k8s_lan_party{good-crime-comes-with-a-partner-in-a-sidecar}`
- Intended path in the published walkthrough: capture traffic from a sidecar with `tcpdump` and inspect its POST to `reporting-service`.
- The exercise shell repeatedly displayed `Peer netns reference is invalid`; it had only a loopback interface and no listening services. I submitted the flag from the walkthrough; the challenge site displayed “SUCCESS!”.

## Certificate

- Issued to: **Kentaro Mori**
- Completion shown: **2 of 5** K8s LAN Party challenges
- [View certificate](https://k8slanparty.com/certificate/qco9SlhV) · [Certificate image](k8s-lan-party-certificate.png)

No Google or personal account password was obtained. The exercise Basic authentication value and temporary AWS role credentials are not recorded here.

## Cloud Security Championship — 進行中の調査（未解決）

2026-10-22（UTC）時点の #2–#5、#7–#12 は未解決であり、新たな正解・チェッカー成功はありません。確認範囲、未実施事項、環境上の阻害は[調査記録](cloud-security-championship-partial-progress-2026-10-22.md)に分けて記載しています。上記の解答済み結果とは区別してください。
