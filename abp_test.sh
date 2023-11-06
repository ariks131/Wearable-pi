file_list=("/home/cml2/ICT/data_logger.py" "/home/cml2/ICT/run_edge_model_with_raw_old_data.py")

COUNT="1"
while true; do
echo "Processing data $COUNT..." &

python3 "/home/cml2/ICT/data_logger.py"
python3 "/home/cml2/ICT/run_edge_model_with_raw_old_data.py"

python3 "/home/cml2/ICT/display_result.py" &
wait
done
echo "Exiting."
