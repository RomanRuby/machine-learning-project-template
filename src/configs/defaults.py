import argparse


def parser_default_init():
    parser = argparse.ArgumentParser()

    # DATA LOCATION
    parser.add_argument('--train_data_dir', type = str,
                        default = 'dataset/train/audio/')
    parser.add_argument('--test_data_dir', type = str,
                        default = 'dataset/test/audio/')

    # FILE ADDITIONAL
    parser.add_argument('--file_words', type = str, default = 'map_words.txt')
    parser.add_argument('--file_chars', type = str, default = 'map_chars.txt')
    # the top num_key_words in map_words.txt are key words
    parser.add_argument('--num_key_words', type = int, default = 10)

    # RESULT DIR
    parser.add_argument('--result_dir', type = str, default = 'logs')
    parser.add_argument('--log_dir', type = str, default = 'run/logs')

    # PROCESSS DATA
    parser.add_argument('--sample_rate', type = int, default = 16000)
    parser.add_argument('--frame_size_ms', type = float, default = 30.0)
    parser.add_argument('--frame_stride_ms', type = float, default = 10.0)

    # fg_interp_factor = target_duration_ms/(target_duration_ms-pad_ms)
    parser.add_argument('--pad_ms', type = float, default = 140)
    parser.add_argument('--target_duration_ms', type = int, default = 1140)
    parser.add_argument('--num_mel_bins', type = int, default = 46)

    # Model
    parser.add_argument('--lr_init', type = float, default = 0.0002)
    parser.add_argument('--lr_drate', type = float, default = 0.3)
    parser.add_argument('--dropout_keep_prob', type = float, default = 0.5)
    parser.add_argument('--l2_scale', type = float, default = 0)

    parser.add_argument('--ckpt_dir', type = str, default = 'run/ckpts')

    parser.add_argument('--bg_nsr', type = float, default = 0.5)
    parser.add_argument('--bg_noise_prob', type = float, default = 0.75)
    parser.add_argument('--unknown_pct', type = float, default = 1 / 6)
    parser.add_argument('--gmem_dynamic', action = 'store_true', default = False)
    # parser.add_argument('--start_ckpt', type = str, default = '')
    parser.add_argument('--num_folds', type = int, default = 5)
    parser.add_argument('--fold_idx', type = int, default = 1)
    parser.add_argument('--batch_size', type = int, default = 128)
    parser.add_argument('--init_valid_epoch', type = float, default = 1)
    parser.add_argument('--num_submissions', type = int, default = 5)
    parser.add_argument('--skip_test', action = 'store_true', default = False)

    # num_batches/lr_dstep = 2.3
    parser.add_argument('--lr_dstep', type = int, default = 3800)
    parser.add_argument('--num_batches', type = int, default = 9000)

    FLAGS, unparsed = parser.parse_known_args()
    return FLAGS, unparsed