dictFinal = {
  '@type': 'MessageCard',
  '@context': 'http://schema.org/extensions',
  'themeColor': '2DC72D',
  'summary': 'HostOutOfMemory',
  'title': 'Prometheus Alert (Resolved)',
  'sections': [
    {
      'activityTitle': '[Node memory is filling up (< 10% left)n  VALUE = 9.410993253703694n  LABELS = map[instance:192.168.0.159:9100 job:nodeproxy servidor:Agataproxybpm]](https://agatabpm.emetel.local/alertmanager)',
      'facts': [
        {
          'name': 'description',
          'value': 'Node memory is filling up (< 10% left)n  VALUE = 9.410993253703694n  LABELS = map[instance:192.168.0.159:9100 job:nodeproxy servidor:Agataproxybpm]'
        },
        {
          'name': 'title',
          'value': 'Host out of memory (instance 192.168.0.159:9100)'
        },
        { 'name': 'alertname', 'value': 'HostOutOfMemory' },
        { 'name': 'instance', 'value': '192.168.0.159:9100' },
        { 'name': 'job', 'value': 'nodeproxy' },
        { 'name': 'servidor', 'value': 'Agataproxybpm' },
        { 'name': 'severity', 'value': 'warning' }
      ],
      'markdown': 'true'
    }
  ]
}

print(dict)