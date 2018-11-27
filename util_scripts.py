def generate_fake_images_label_janers(run_id, snapshot=None, grid_size=[1,1], num_pngs=100, image_shrink=1, png_prefix=None, random_seed=1000, minibatch_size=8):
    #with open('output_5000.tsv', 'w') as out_file:
        #tsv_writer = csv.writer(out_file, delimiter='\t')
        network_pkl = misc.locate_network_pkl(run_id, snapshot)
        if png_prefix is None:
            png_prefix = misc.get_id_string_for_network_pkl(network_pkl) + '-'
        random_state = np.random.RandomState(random_seed)


        #tf.reduce_mean(x, 0)
        print('Loading network from "%s"...' % network_pkl)
        G, D, Gs = misc.load_network_pkl(run_id, snapshot)
        counter=0
        result_subdir = misc.create_result_subdir(config.result_dir, config.desc)
        for png_idx in range(num_pngs):
            print('Generating png %d / %d...' % (png_idx, num_pngs))
            latents = misc.random_latents(np.prod(grid_size), Gs, random_state=random_state)
            print("sum latents", np.sum(latents))
            print("mean latents", np.mean(latents))

            print(latents.shape)
            labels=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

            labels_arr=np.array(labels)
            x = np.reshape(labels_arr, (1, 19))
            #labels = np.zeros([latents.shape[0], 0], np.float32)
            print(x.shape)
            images = Gs.run(latents, x, minibatch_size=minibatch_size, num_gpus=config.num_gpus, out_mul=127.5, out_add=127.5, out_shrink=image_shrink, out_dtype=np.uint8)
            misc.save_image_grid(images, os.path.join(result_subdir, '%s%06d.png' % (png_prefix, png_idx)), [0,255], grid_size)
        open(os.path.join(result_subdir, '_done.txt'), 'wt').close()
