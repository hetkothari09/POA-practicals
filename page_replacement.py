no_pages = int(input("Enter total number of Pages: "))
pages = []
for i in range(no_pages):
    page = int(input(f"Enter page {i+1}: "))
    pages.append(page)

no_frames = int(input("Enter total number of Frames: "))

def fifo(pages, no_fr):
    frames = [-1] * no_frames
    miss = 0
    
    print("\nFIFO:")
    
    for page in pages:
        if page not in frames:
            if -1 in frames:
                frame_no = frames.index(-1)
                frames[frame_no] = page
            else:
                frames.pop(0)
                frames.append(page)
            miss += 1
            print("\tMISS", end=" ")
        else:
            print("\tHIT", end=" ")
        
        print("Frames:", frames)

    print(f"\nMisses = {miss}/{len(pages)}")
    print(f"Hits   = {len(pages) - miss}/{len(pages)}")

def lru(pages, no_fr):
    frames = [-1] * no_frames
    time_used = [0] * len(frames)
    miss = 0

    print("\nLRU:")
    for page in pages:
        if page not in frames:
            if -1 in frames:
                frame_no = frames.index(-1)
                frames[frame_no] = page
                time_used[frame_no] = time_used[frame_no - 1] + 1 if frame_no > 0 else 1
            else:
                oldest_frame_index = time_used.index(min(time_used))
                frames[oldest_frame_index] = page
                time_used[oldest_frame_index] = 1
            miss += 1
            print("\tMISS", end=" ")
        else:
            frame_index = frames.index(page)
            time_used[frame_index] += 1
            print("\tHIT", end=" ")
        
        print("Frames:", frames)

    print(f"\nMisses = {miss}/{len(pages)}")
    print(f"Hits   = {len(pages) - miss}/{len(pages)}")


def optimal(pages, no_frames):
    frames = [-1] * no_frames
    miss = 0

    print("\nOptimal:")
    for page in pages:
        if page not in frames:
            if -1 in frames:
                frame_no = frames.index(-1)
                frames[frame_no] = page
            else:
                future_pages = pages[pages.index(page):]
                indexes = {frame: future_pages.index(frame) if frame in future_pages else len(future_pages) for frame in frames}
                frame_to_replace = max(indexes, key=indexes.get)
                frames[frames.index(frame_to_replace)] = page
            miss += 1
            print("\tMISS", end=" ")
        else:
            print("\tHIT", end=" ")
        
        print("Frames:", frames)

    print(f"\nMisses = {miss}/{len(pages)}")
    print(f"Hits   = {len(pages) - miss}/{len(pages)}")

fifo(pages, no_frames)
lru(pages, no_frames)
optimal(pages, no_frames)
