# crontab 知识点总结

**curator中的 crontab 示例：**

```yaml
55 */3 * * * /export/servers/es-curator/curator/hb-cdnbak-es/curator-delete-index.sh >>/export/work/Logs/hb-cdnbak-es_curator-delete-index.log

20 15 * * * /export/servers/es-curator/curator/hb-es-cdn-new/curator-delete-index.sh >>/export/work/Logs/hb-es-cdn-new_curator-delete-index.log

35 16 * * * /export/servers/es-curator/curator/hb-cdn-es/curator-delete-index.sh >>/export/work/Logs/hb-cdn-es_curator-delete-index.log

30 */1 * * * /export/servers/es-curator/curator/hb-qkh-es/curator-delete-index.sh >>/export/work/Logs/hb-qkh-es_curator-delete-index.log

30 */5 * * * /export/servers/es-curator/curator/hb-bj02-es-qkh-bak/curator-delete-index.sh >>/export/work/Logs/hb-bj02-es-qkh-bak_curator-delete-index.log

55 */5 * * * /export/servers/es-curator/curator/hb-es-public/curator-delete-index.sh >>/export/work/Logs/hb-es-public_curator-delete-index.log

30 9 * * * /export/servers/es-curator/curator/hb-es-cdnlive/curator-delete-index.sh >>/export/work/Logs/hb-es-cdnlive_curator-delete-index.log

30 * * * * /export/servers/es-curator/curator/hb-zyx-es-log-ddos/curator-delete-index.sh >>/export/work/Logs/hb-zyx-es-log-ddos_curator-delete-index.log

18 */6 * * * /export/servers/es-curator/curator/es-nlb-es-v2cjz7a2ir/curator-delete-index.sh >>/export/work/Logs/es-nlb-es-mkm9fksd1q_curator-delete-index.log

20 */3 * * * /export/servers/es-curator/curator/hb-log-es/curator-delete-index.sh >>/export/work/Logs/hb-log-es_curator-delete-index.log

10 */2 * * * /export/servers/es-curator/curator/hb-tsdb-es2/curator-delete-index.sh >>/export/work/Logs/hb-tsdb-es2_curator-delete-index.log

05 */1 * * * /export/servers/es-curator/curator/hb-zyx-es-ark-log-devops/curator-delete-index.sh >>/export/work/Logs/hb-zyx-es-ark-log-devops_curator-delete-index.log

40 */5 * * * /export/servers/es-curator/curator/hb-zyx-es-public2/curator-delete-index.sh >>/export/work/Logs/hb-zyx-es-public2_curator-delete-index.log

10 */6 * * * /export/servers/es-curator/curator/es-nlb-es-uddmdr2i9w/curator-delete-index.sh >>/export/work/Logs/es-nlb-es-uddmdr2i9w_curator-delete-index.log

15 */6 * * * /export/servers/es-curator/curator/hb-sre-es/curator-delete-index.sh >>/export/work/Logs/hb-sre-es_curator-delete-index.log

25 23 * * * /export/servers/es-curator/curator/lf-monitor-es/curator-delete-index.sh >>/export/work/Logs/lf-monitor-es_curator-delete-index.log

20 */3 * * * /export/servers/es-curator/curator/ht-es-traffic-analysis/curator-delete-index.sh >>/export/work/Logs/ht-es-traffic-analysis_curator-delete-index.log
```

