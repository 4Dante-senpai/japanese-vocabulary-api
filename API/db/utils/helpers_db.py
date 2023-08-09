def generate_metadata(page):
    
    meta = {
        'page' : page.page,
        'pages' : page.pages,
        'per_page' : page.per_page,
        'total_count': page.total,
        'prev_page' : page.prev_num,
        'next_page' : page.next_num,
        'has_prev' : page.has_prev,
        'has_next' : page.has_next
    }

    return meta
