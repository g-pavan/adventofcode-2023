class SeedSolver:
    def __init__(self, info):
        lines = info.split("\n")[1:]
        # Dest Src Size
        self.mapping = [[int(x) for x in line.split()] for line in lines]

    def findMapping(self, x):
        for (dest,src,size) in self.mapping:
            if src <= x < src + size:
                return dest + x - src
        return x

    def findRanges(self, _range):
        ans = []
        for dest,src,size in self.mapping:
            src_end = src + size
            new_range = []
            while _range:
                (start,end) = _range.pop()
                # [src src_end) might cut this range

                # No overlap condition
                if end < src or src_end < start:
                    new_range.append((start,end))
                else:
                    # They are overlapping.
                    # 4 possible overlaps: Let's explore them all
                    # 1. [src---start---src_end---end]
                    # 2. [src---start---end---src_end]
                    # 3. [start-----src---end---src_end]
                    # 4. [start----src---src_end----end]

                    # 1. [src---start---src_end---end]
                    if src <= start and src_end <= end:
                        overlap_range = (start,src_end)
                        ans.append((overlap_range[0]-src+dest, overlap_range[1]-src+dest))

                        non_overlap_right = (src_end,end)
                        if non_overlap_right[1] > non_overlap_right[0]:
                            new_range.append(non_overlap_right)
                    
                    # 2. [src---start---end---src_end]
                    elif src <= start and end <= src_end:
                        overlap_range = (start,end)
                        ans.append((overlap_range[0]-src+dest, overlap_range[1]-src+dest))
                    
                    # 3. [start-----src---end---src_end]
                    elif start <= src and end <= src_end:
                        overlap_range = (src,end)
                        ans.append((overlap_range[0]-src+dest, overlap_range[1]-src+dest))

                        non_overlap_left = (start,src)
                        if non_overlap_left[1] > non_overlap_left[0]:
                            new_range.append(non_overlap_left)
                    
                    # 4. [start----src---src_end----end]
                    elif start <= src and src_end <= end:
                        overlap_range = (src,src_end)
                        ans.append((overlap_range[0]-src+dest, overlap_range[1]-src+dest))

                        # 2 new ranges are formed
                        non_overlap_left = (start,src)
                        non_overlap_right = (src_end,end)
                        if non_overlap_left[1] > non_overlap_left[0]:
                            new_range.append(non_overlap_left)
                        if non_overlap_right[1] > non_overlap_right[0]:
                            new_range.append(non_overlap_right)

            _range = new_range
        return ans + _range


def solve_1(seeds, mappings):
    ans = 10**100
    for s in seeds:
        for maps in mappings:
            s = maps.findMapping(s)
        ans = min(ans,s)
    return ans

def solve_2(seeds, mappings):
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    ans = 10**100
    # Store the ranges as [a,b)
    for start, size in seed_pairs:
        _range = [(start, start+size)]
        for maps in mappings:
            _range = maps.findRanges(_range)
        ans = min(ans, min(_range)[0])
    return ans

if __name__ == "__main__":
    lines = open("input.txt","r").read()
    seeds, *others = lines.split("\n\n")
    seeds = [int(x) for x in seeds.split(":")[1].split()]
    mappings = [SeedSolver(s) for s in others]

    # print('Part 1: ',solve_1(seeds, mappings))
    print('Part 2: ',solve_2(seeds,mappings))
