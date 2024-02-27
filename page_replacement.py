pages = [6, 0, 12, 0, 30, 4, 2, 30, 32, 1, 20, 15]
no_fr = int(input("Enter total number of Frames: "))

def fifo(pages, no_fr):
    frames = [-1] * no_fr
    in_time = [0] * len(pages)
    miss = 0
    
    print("\nFIFO:")
    for time, page in enumerate(pages):
        min_t = in_time[0]
        oldest_page = 0
        page_assigned = False
        if page not in frames:
            for frame_no, frame in enumerate(frames):
                if frame == -1:
                    frames[frame_no] = page
                    in_time[frame_no] = time
                    page_assigned = True
                    miss += 1
                    break

                if in_time[frame_no] < min_t:
                    min_t = in_time[frame_no]
                    oldest_page = frame_no
        
            if not page_assigned:
                frames[oldest_page] = page
                in_time[oldest_page] = time
                miss += 1
        
        print("For ", page, "-", frames)

    print(f"\nMisses = {miss}/{len(pages)}")
    print(f"Hits   = {len(pages) - miss}/{len(pages)}")

def lru(pages, no_fr):
    frames = [-1] * no_fr
    time_used = [0] * len(pages)
    miss = 0

    print("\nLRU:")
    for time, page in enumerate(pages):
        min_t = time_used[0]
        oldest_used_page = 0
        page_assigned = False

        if page not in frames:
            for frame_no, frame in enumerate(frames):
                if frame == -1:
                    frames[frame_no] = page
                    time_used[frame_no] = time
                    page_assigned = True
                    miss += 1
                    break

                if time_used[frame_no] < min_t:
                    min_t = time_used[frame_no]
                    oldest_used_page = frame_no
        
            if not page_assigned:
                frames[oldest_used_page] = page
                time_used[oldest_used_page] = time
                miss += 1

        else:
            page_found_at = frames.index(page)
            time_used[page_found_at] = time
            
        
        print("For ", page, "-", frames)

    print(f"\nMisses = {miss}/{len(pages)}")
    print(f"Hits   = {len(pages) - miss}/{len(pages)}")


def optimal(pages, no_fr):
    frames = [-1] * no_fr
    miss = 0

    print("\nOptimal:")
    for time, page in enumerate(pages):
        if page not in frames:
            if -1 in frames:
                frame_no = frames.index(-1)
                frames[frame_no] = page
                miss += 1
            
            else:
                future_pages = pages[time + 1: time + 1 + no_fr]
                frame_future_freq = [future_pages.count(frame) for frame in frames]

                min_future_freq = min(frame_future_freq)
                frames[frame_future_freq.index(min_future_freq)] = page
                miss += 1
        
        print("For ", page, "-", frames)

    print(f"\nTotal Misses = {miss}/{len(pages)}")
    print(f"Total Hits   = {len(pages) - miss}/{len(pages)}")
    pass


fifo(pages, no_fr)
lru(pages, no_fr)
optimal(pages, no_fr)