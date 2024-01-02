from lingrex.copar import CoPaR

# Load data into CoPaR and create patterns
cop = CoPaR('bpt_alg.tsv', transcription='form', ref='cogid', min_refs=3)
cop.get_sites()
cop.cluster_sites()
cop.sites_to_pattern()
cop.add_patterns()

# Write output
cop.write_patterns('d_patterns.tsv')
