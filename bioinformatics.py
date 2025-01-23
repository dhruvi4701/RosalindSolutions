def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

dna_sequence = "ATCGATCGATCG"
gc_percentage = gc_content(dna_sequence)

print(f"GC content: {gc_percentage:.2f}%")
